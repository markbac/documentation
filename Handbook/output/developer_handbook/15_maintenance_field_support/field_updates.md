# Field Updates

This page outlines standard workflows for Over-the-Air (OTA) and field-programming updates to deployed hardware. It describes required procedures, accepted tools, risk management principles, and key engineering considerations to ensure reliable and secure field updates.

---

## 1. Overview

Field updates enable deployed devices to receive firmware, software, or configuration changes after production. These processes are critical for delivering features, ensuring regulatory compliance, addressing vulnerabilities, and maintaining device performance. The two principal approaches are:

- **Over-the-Air (OTA) Updates**: Update is delivered remotely via network connectivity.
- **Field-Programming Updates**: Update requires direct physical intervention (e.g., JTAG, USB, SD card).

Both methods require careful management to prevent bricking, downtime, or security incidents.

---

## 2. OTA Update Workflow

### 2.1. Preparation

- **Versioning**: Every release must have a unique, unambiguous version identifier (semantic versioning recommended). Version metadata must be embedded in the update package.
- **Integrity and Authenticity**: All OTA packages must be digitally signed. The public key should be securely embedded in the device at manufacturing.
- **Backward Compatibility**: Device firmware must gracefully handle unknown or unsupported update formats/versions. Downgrade (roll-back) paths must be considered.

### 2.2. Delivery Mechanisms

- **Pull**: Device polls a secure update server at defined intervals.
- **Push**: Server notifies the device of update availability (often via MQTT, webhooks, or SMS for low-power devices).

Most architectures prefer the pull model for scalability and reliability.

### 2.3. Update Process

1. **Pre-Update Validation**
   - Check reliable network connectivity.
   - Verify available battery/power (updates must not brick the device due to a brownout).
   - Confirm sufficient free storage.

2. **Download**
   - Download update to a non-volatile scratch area separate from the live firmware partition.
   - Verify digital signature before applying.

3. **Installation**
   - Enter an 'update mode'; quiesce or gracefully suspend active tasks as required.
   - Apply update atomically where hardware allows (e.g., A/B partitioning). Never overwrite live firmware directly unless hardware is tolerant of interruptions.
   - OPTIONAL: Backup essential configuration or user data before the update.

4. **Verification and Recovery**
   - Reboot into the new firmware.
   - Self-check critical functionality (bootloader checks, heartbeats).
   - If verification fails, automatically revert to the previous working firmware (fallback).

### 2.4. Post-Update Steps

- Report update completion and new version to the management server.
- Log update events to persistent storage for audit.
- Clear temporary update files.

### 2.5. Security Considerations

- Never allow unsigned or expired updates, even in test environments.
- Periodically update cryptographic keys using secure distribution.
- Protect update-related APIs with authentication and authorisation.

#### Example: Secure OTA Firmware Update Sequence

1. Device downloads signed update from HTTPS server.
2. Device verifies update signature using pre-installed public key.
3. Update is written to inactive partition (B).
4. Device reboots into partition B.
5. Device runs post-update self-check; if passed, marks partition B as active.
6. If failed, device rolls back to previous partition (A) automatically.

---

## 3. Field-Programming Workflow

### 3.1. When to Use Field Programming

- Device lacks reliable network connectivity.
- Major hardware changes require manual intervention.
- Factory rework or recovery from failed OTA.

### 3.2. Methods

- **Physical Connection**: JTAG, UART, USB, or dedicated programmer port.
- **Removable Media**: SD card or USB drive loaded with update file.

### 3.3. Required Procedure

1. **Preparation**
   - Acquire firmware image verified with checksum and signature.
   - Ensure correct programming tool and access rights.
   - Power off device using documented safe shutdown process.

2. **Programming**
   - Connect programmer using documented pin-out.
   - Authenticate session if supported (e.g., password or challenge-response).
   - Erase target memory area before flashing.
   - Program firmware; verify written data byte-for-byte.

3. **Verification**
   - Power-cycle or soft-reset device.
   - Confirm correct boot and core functionality through in-field tests.

4. **Documentation**
   - Log device serial, version, update time, operator, and reason.
   - Submit logs to central asset management system.

### 3.4. Field Programming Best Practices

- Never attempt field-programming with low or unstable power supply.
- Use ESD protection when handling open electronics.
- Retain older firmware and release notes for possible reversions.
- Physically secure access to programming ports to prevent unauthorised modification.

#### Example: USB-Based Field Update

1. Technician downloads signed update onto FAT-formatted USB.
2. Device is powered off and update USB inserted.
3. Device is powered on in 'update detection' mode, indicated by amber LED.
4. Device validates file and flashes firmware.
5. Device reboots; LED changes to green.
6. Technician verifies functionality, removes USB, and logs completion.

---

## 4. Risk Management and Support

- Design firmware with robust bootloader and failsafe mechanisms.
- Maintain up-to-date, field-ready rescue images.
- Document the precise, supported workflow for both OTA and field updates in product manuals and technical notes.
- Provide clear status indicators (LED, display, logs) for update state and errors.

---

## 5. Troubleshooting and Rollback

- Always have a tested, automated recovery path in case updates fail (e.g., dual partitions, watch-dog reset).
- Maintain a log of all update attempts and outcomes, accessible both locally and centrally.
- Communicate clearly with field teams and support staff, providing checklists for common failures: power loss, authentication errors, corruption, incompatibility.

---

## 6. Summary of Expectations

- All updates, OTA or field, must be secure, traceable, and reversible.
- Updates must never compromise device safety, data, or compliance posture.
- Every field update event must be logged with sufficient metadata for future audit.

For more detailed references, consult the respective product's Field Maintenance Standard Operating Procedures (SOPs) and Security Guidelines.