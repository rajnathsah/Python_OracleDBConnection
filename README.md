# Python Oracle Database Connection
Access Oracle database from python

### Pre-requisite for accessing oracle database from python
1. Install cx_Oracle using pip from PyPI
  Using following command cx_Oracle can be installed and upgraded. </br>
  ```python 
  pip install cx_Oracle --upgrade
  ```
2. Install Oracle client or Oracle instant client if Oracle client is not installed on the machine accessing database where python is intended to run. 
#### Oracle instance client installation
Download an Oracle 18, 12, or 11.2 “Basic” or “Basic Light” zip file: [64-bit](https://www.oracle.com/technetwork/topics/winx64soft-089540.html) or [32-bit](https://www.oracle.com/technetwork/topics/winsoft-085727.html), matching your Python architecture.

Extract zip file to any location and update environment variable by including the path of extracted folder. For more details, please refer [cx_Oracle](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html) installation document.  

Another userful link from oracle on getting started with [cx_Oracle](https://developer.oracle.com/databases/database-for-python-developers-1.html) with examples. 

File dbconnection.py has example to select and insert data, it also has example of executing function and procedure from python.

## Access Oracle cloud database using Python
### Setup Oracle autonomous database 
1. Setup always free autonomous database using [link](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/autonomous-always-free.html#GUID-03F9F3E8-8A98-4792-AB9C-F0BACF02DC3E).  
2. Follow the [link](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connecting-nodejs.html#GUID-AB1E323A-65B9-47C4-840B-EC3453F3AD53) to connect to database from python.
3. Use cloud_databaseconnection.py sample program to test the connectivity.

Happy Learning!
