su is used to change the current user to betty.

id -un is used to print the effective username of the current user.

id -Gn is used to print all the groups the current user is part of.

chown betty hello is used to change the ownership of a file to the user betty.

touch hello is used to create a new empty file.

chmod u+x is used to change the execution of a file.

chmod ug+x,o+r allows the owner and group owner to execute the file, while the others can't read it.

chmod ugo+x is used to allow everybody to do anything to the file.

chmod 007 is used to give permission to other users, but not the owner or group owner.

chmod 753 is used to set the mode of the file.

chmod --reference==olleh used to set the mode of hello as olleh.

chmod -R +X .  Add execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.

mkdir -m used to create a new directory with certain permissions (add the code of the permissions before the directory name).

chgrp (new group) file is used to change the ownership of a file to a certain group.

chown vincent:staff * to change the owner and group owner.

chown vincent:staff (file name) to change a certain file's owner and group owner.

chown --from==(specified user) newuser file.

telnet towel.blinkenlights.nl will play the StarWars IV episode in the terminal.
