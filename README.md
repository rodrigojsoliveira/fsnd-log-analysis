# Log Analysis
This tool will print reports from data in a mock database for a fictional news website.
The database contains three tables: articles, authors and log. By using SELECT queries and SQL joins
the reporting tool will answer the folowing three questions:

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors?

## Virtual Machine Setup
In order to run the code, you will need to install some software. They are:

1. VirtualBox. This is virtualization software that will let you run a virtual machine on your computer. Visit https://www.virtualbox.org/, download the package for your system and install it.
1. Vagrant. Vagrant is a tool for building and managing virtual machine environments. Download it at https://www.vagrantup.com/.

After installing both softwares you will use the virtual machine configuration file inside *FSND-Virtual-Machine.zip"*. Unzip the archive to a new directory, change into it and you should find a folder called **vagrant**.

Change into the **vagrant** folder and type `vagrant up`. This will set up a Linux environment. This step may take a few minutes.

When you see your shell prompt again, type `vagrant ssh` and you will log into your new Linux virtual machine. You should see a shell prompt starting with the word *vagrant*.

Change to folder `/vagrant`. This folder is shared between your computer and the virtual machine, so you should be able to edit code and run it on your VM.

## Configuring the Database
A PostgreSQL database should already be configured in the VM for you. You can use the `psql` command to access it.

Now you will create the tables and populate them with data. To do this, download file **newsdata.zip**, unzip it into the `vagrant` folder shared between your computer and the VM. You should see a file called `newsdata.sql`.

Change into the `vagrant` folder using the command line, and type `psql -d news -f newsdata.sql`. Once done, you should be ready to run the Python code.

## Python version
You will need Python 3 installed on your system to run the log analysis tool.

## Dependencies
This tool used **psycopg2** module to to connect to the database and run SQL queries.
To install the module, please refer to psycopg2's website at http://initd.org/psycopg/docs/install.html#binary-install-from-pypi.

## Running the code
Be sure you place file `log_analysis.py` inside your `vagrant` folder to run it on the VM.
Once inside the folder, type `./log_analysis.py` to run. After a few seconds, the first results should appear on screen.
File `sample_output.txt` contains the expected results after program completion.





