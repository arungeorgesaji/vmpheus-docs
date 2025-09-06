Connection
=====================

Windows Connection
--------------------

You can use **mstsc** to connect to the Windows VM you were given. It is a built-in tool for Remote Desktop Connection.

Run the following command in your terminal or Run window:

.. code-block:: console

   mstsc /v:<IP_ADDRESS> /prompt

Use the username and password provided to you when prompted.

If you don't know what an IP address is, it's those numbers separated by dots (for example, 192.168.0.1). 

Linux Connection
--------------------

If you are unsure if you are on xorg or wayland, please ask for help(P.S: You probbly should be knowing this). Also you can use any tool which supports RDP for connection...

You might need to install a RDP supporting tool(We recommend xfreerdp for xorg and wfreerdp for wayland and have provided provided instructions for them below)(P.S: If you are on linux just use your package manager for doing this also the binary name might be different on your system so adjust command accordingly).

Xorg Connection
~~~~~~~~~~~~~~~~~~~~

You can use **xfreerdp** to connect to the VM you were given if you are on xorg.


.. code-block:: console

  xfreerdp /v:IP_ADDRESS /u:username /p:'password' /sec:rdp 

If you don't know what an IP address is, it's those numbers separated by dots (for example, 192.168.0.1). 

Wayland Connection(Untested)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use **wfreerdp** to connect to the VM you were given if you are on wayland.


.. code-block:: console

  wfreerdp /v:IP_ADDRESS /u:username /p:'password' /sec:rdp 

If you don't know what an IP address is, it's those numbers separated by dots (for example, 192.168.0.1). 

MacOS Connection 
--------------------

Sorry we don't have any instructions for MacOS users yet. Please do it yourself also consider contributing to the docs by adding instructions for MacOS users. 
