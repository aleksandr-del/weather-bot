# Linux Server Management Tips

## System Service Management

### Understanding `sudo apt dist-upgrade`
- Performs intelligent upgrade of all packages to latest versions
- Handles dependency changes by installing/removing packages as needed
- More aggressive than `apt upgrade` - can modify package dependency structure
- Can upgrade kernel and core system components
- Always run `sudo apt update` first to refresh package lists

### Managing Background Processes
- `jobs` only shows processes from current shell session
- Use `ps aux` to see all running processes
- Find specific processes: `ps aux | grep process_name`
- Kill processes: `kill <PID>` or `kill -9 <PID>` for force kill
- Processes can persist after SSH disconnection if started with `nohup` or `&`

## Disk Space Management

### Check Disk Usage
```bash
df -h                    # Human-readable disk usage for all filesystems
df -h .                  # Check current directory
du -h --max-depth=1      # Directory usage breakdown
du -sh .                 # Total usage of current directory
```

## Systemd Service Configuration

### Service Unit File Structure
```ini
[Unit]
Description=service_name
After=syslog.target
After=network.target

[Service]
Type=simple
User=username
WorkingDirectory=/path/to/app
ExecStart=/path/to/executable
Restart=always

[Install]
WantedBy=multi-user.target
```

### Service Management Commands
```bash
sudo systemctl daemon-reload    # Reload service files
sudo systemctl enable service   # Enable auto-start on boot
sudo systemctl start service    # Start service
sudo systemctl status service   # Check service status
```

## Log Management

### Viewing Service Logs
```bash
journalctl -u service_name           # View service logs
journalctl -u service_name -f        # Follow logs in real-time
journalctl -u service_name -n 50     # Show last 50 lines
journalctl --disk-usage              # Check total log size
```

### Log Retention Configuration
Edit `/etc/systemd/journald.conf`:
```ini
SystemMaxUse=100M        # Maximum total log size
SystemMaxFileSize=10M    # Maximum single log file size
MaxRetentionSec=1month   # Delete logs older than 1 month
```

### Manual Log Cleanup
```bash
sudo journalctl --vacuum-time=2d     # Keep only last 2 days
sudo journalctl --vacuum-size=50M    # Keep only 50MB of logs
```

## Best Practices

### Service Security
- Run services as specific users (not root)
- Set appropriate working directories
- Configure log retention to prevent disk filling
- Use `Restart=always` for critical services

### System Monitoring
- Regularly check disk space with `df -h`
- Monitor running processes with `ps aux`
- Check service logs for errors
- Set up log rotation and cleanup

### SSH Session Management
- Use `Ctrl+C` to stop processes before closing SSH
- Use `nohup command &` if you want processes to persist
- Check for orphaned processes after disconnection
