lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
sudo parted /dev/sda --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo mkfs.xfs /dev/sda -f
sudo partprobe /dev/sda
sudo mount dev/sda /mnt2
sudo blkid
sudo nano /etc/fstab

# then add uuid so drive is automaticly loaded 