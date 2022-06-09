lsblk -o NAME,HCTL,SIZE,MOUNTPOINT | grep -i "sd"
sudo parted /dev/sda --script mklabel gpt mkpart xfspart xfs 0% 100%
sudo mkfs.xfs /dev/sda -f
sudo partprobe /dev/sda
sudo mount dev/sda /mnt2
sudo blkid

# then add uuid so drive is automaticly loaded 

sudo nano /etc/fstab
# UUID=4e6d8537-8011-476f-9cd4-dc29e9799577   /datadrive   xfs   defaults,nofail   1   2

# set permission on mnt2
# go to root
cd /
sudo chmod 777 mnt2
