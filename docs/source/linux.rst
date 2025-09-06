Linux Usage
=============

We recommend using containers even if you are testing a program which runs natively on ubuntu like .deb and elf binaries as to not cause weird dependency issues for everyone. We recommend using distrobox for this(distrobox should already be setup if not please report this).

Create container 
-----------------

.. code-block:: bash

    distrobox create -n container_name -i  image_name

You can find a list of all the offficially tested containers from docker with this tool at https://distrobox.it/compatibility/ in the Containers Distros section.

Enter container 
-----------------

.. code-block:: bash

    distrobox enter container_name

Usage 
-----------------

Once inside the container you can use the same commands as in the other OS sections. If you need to install any dependencies please do so with the package manager of your container's distro.

Use 'exit' to leave the container when you are done.
