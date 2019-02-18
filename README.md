# interview_challenge

## Short description
This repo is the solution to an interview challenge. The main goal is to generate a setup with mysql, nginx and an app that show the result of a particular query.

## Minimun requirements

Software | Version
:------------- | -------------:
docker-compose | 3.4+
docker | 17.09.0+

## Step by step guide (simple version)

This guide (simple version) uses the images already generated and available at dockerhub. If you want to build locally the app image check [here](#using-local-image-example).

First install [docker](https://docs.docker.com/install/)  & [docker-compose](https://docs.docker.com/compose/install/).

Then run the following to clone the repo and start the containers

```
git clone git@github.com:Juanchimienti/interview_challenge.git
cd interview_challenge
git submodule update --init --recursive

docker-compose up
```

This will start 3 containers (nginx, app, db) and open the port 8080 on your local machine.

Then point the browser to http://127.0.0.1:8080/employees/custom_list and you should see the list of employees.

The first time that you start the enviroment the mysql database gets populated as a result. It will take a few minutes to be ready (in my computer it took 5 minutes). You should wait for the "mysqld: ready for connections." message to appear in the console.

Once you wish to stop just press Ctrl-C.

## Example run

```
$ docker-compose up
Pulling app (juanchimienti/interview_challenge_app:0.1.1)...
0.1.1: Pulling from juanchimienti/interview_challenge_app
6c40cc604d8e: Already exists
eb28c72fd5c9: Pull complete
8b7b7e8a3ec6: Pull complete
07400c149ca6: Pull complete
ec0154d44b37: Pull complete
f312a8f3b160: Pull complete
42861ec7e6a3: Pull complete
f752a85cdd37: Pull complete
Pulling db (mariadb:10.4)...
10.4: Pulling from library/mariadb
6cf436f81810: Pull complete
987088a85b96: Pull complete
b4624b3efe06: Pull complete
d42beb8ded59: Pull complete
5badffea4c42: Pull complete
6107652a946b: Pull complete
1b31669dbe65: Pull complete
4d884b22dc63: Pull complete
cee72f2b293c: Pull complete
33323ef67397: Pull complete
2dee316773b8: Pull complete
e6c593fc6d14: Pull complete
21812f999f9e: Pull complete
5e4cb67f14ee: Pull complete
Creating interview_challenge_nginx_1 ... done
Creating interview_challenge_app_1   ... done
Creating interview_challenge_db_1    ... done
Attaching to interview_challenge_app_1, interview_challenge_db_1, interview_challenge_nginx_1
app_1    | [2019-02-17 03:22:24 +0000] [1] [INFO] Starting gunicorn 19.9.0
app_1    | [2019-02-17 03:22:24 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
app_1    | [2019-02-17 03:22:24 +0000] [1] [INFO] Using worker: sync
app_1    | [2019-02-17 03:22:24 +0000] [8] [INFO] Booting worker with pid: 8
app_1    | [2019-02-17 03:22:24 +0000] [9] [INFO] Booting worker with pid: 9
app_1    | [2019-02-17 03:22:24 +0000] [10] [INFO] Booting worker with pid: 10
app_1    | [2019-02-17 03:22:24 +0000] [11] [INFO] Booting worker with pid: 11
app_1    | [2019-02-17 03:22:24 +0000] [12] [INFO] Booting worker with pid: 12
db_1     | Initializing database
db_1     |
db_1     |
db_1     | PLEASE REMEMBER TO SET A PASSWORD FOR THE MariaDB root USER !
db_1     | To do so, start the server, then issue the following commands:
db_1     |
db_1     | '/usr/bin/mysqladmin' -u root password 'new-password'
db_1     | '/usr/bin/mysqladmin' -u root -h  password 'new-password'
db_1     |
db_1     | Alternatively you can run:
db_1     | '/usr/bin/mysql_secure_installation'
db_1     |
db_1     | which will also give you the option of removing the test
db_1     | databases and anonymous user created by default.  This is
db_1     | strongly recommended for production servers.
db_1     |
db_1     | See the MariaDB Knowledgebase at http://mariadb.com/kb or the
db_1     | MySQL manual for more instructions.
db_1     |
db_1     | Please report any problems at http://mariadb.org/jira
db_1     |
db_1     | The latest information about MariaDB is available at http://mariadb.org/.
db_1     | You can find additional information about the MySQL part at:
db_1     | http://dev.mysql.com
db_1     | Consider joining MariaDB's strong and vibrant community:
db_1     | https://mariadb.org/get-involved/
db_1     |
db_1     | Database initialized
db_1     | MySQL init process in progress...
db_1     | 2019-02-17  3:22:29 0 [Note] mysqld (mysqld 10.4.2-MariaDB-1:10.4.2+maria~bionic) starting as process 104 ...
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Using Linux native AIO
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Uses event mutexes
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Number of pools: 1
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Using SSE2 crc32 instructions
db_1     | 2019-02-17  3:22:29 0 [Note] mysqld: O_TMPFILE is not supported on /tmp (disabling future attempts)
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Initializing buffer pool, total size = 256M, instances = 1, chunk size = 128M
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Completed initialization of buffer pool
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: 128 out of 128 rollback segments are active.
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Creating shared tablespace for temporary tables
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Waiting for purge to start
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: 10.4.2 started; log sequence number 139812; transaction id 21
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
db_1     | 2019-02-17  3:22:29 0 [Note] Plugin 'FEEDBACK' is disabled.
db_1     | 2019-02-17  3:22:29 0 [Warning] 'user' entry 'root@1008b30fb58f' ignored in --skip-name-resolve mode.
db_1     | 2019-02-17  3:22:29 0 [Warning] 'user' entry '@1008b30fb58f' ignored in --skip-name-resolve mode.
db_1     | 2019-02-17  3:22:29 0 [Warning] 'proxies_priv' entry '@% root@1008b30fb58f' ignored in --skip-name-resolve mode.
db_1     | 2019-02-17  3:22:29 0 [Note] InnoDB: Buffer pool(s) load completed at 190217  3:22:29
db_1     | 2019-02-17  3:22:29 0 [Note] Reading of all Master_info entries succeded
db_1     | 2019-02-17  3:22:29 0 [Note] Added new Master_info '' to hash table
db_1     | 2019-02-17  3:22:29 0 [Note] mysqld: ready for connections.
db_1     | Version: '10.4.2-MariaDB-1:10.4.2+maria~bionic'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution
db_1     | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
db_1     | 2019-02-17  3:23:12 10 [Warning] 'proxies_priv' entry '@% root@1008b30fb58f' ignored in --skip-name-resolve mode.
db_1     |
db_1     | /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/load_test_db.sh
db_1     | INFO
db_1     | CREATING DATABASE STRUCTURE
db_1     | INFO
db_1     | storage engine: InnoDB
db_1     | INFO
db_1     | LOADING departments
db_1     | INFO
db_1     | LOADING employees
db_1     | INFO
db_1     | LOADING dept_emp
db_1     | INFO
db_1     | LOADING dept_manager
db_1     | INFO
db_1     | LOADING titles
db_1     | INFO
db_1     | LOADING salaries
db_1     | data_load_time_diff
db_1     | 00:00:22
db_1     |
db_1     | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/test_db
db_1     |
db_1     | 2019-02-17  3:23:35 0 [Note] mysqld (initiated by: unknown): Normal shutdown
db_1     | 2019-02-17  3:23:35 0 [Note] Event Scheduler: Purging the queue. 0 events
db_1     | 2019-02-17  3:23:35 0 [Note] InnoDB: FTS optimize thread exiting.
db_1     | 2019-02-17  3:23:35 0 [Note] InnoDB: Starting shutdown...
db_1     | 2019-02-17  3:23:35 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/ib_buffer_pool
db_1     | 2019-02-17  3:23:35 0 [Note] InnoDB: Instance 0, restricted to 4096 pages due to innodb_buf_pool_dump_pct=25
db_1     | 2019-02-17  3:23:35 0 [Note] InnoDB: Buffer pool(s) dump completed at 190217  3:23:35
db_1     | 2019-02-17  3:23:37 0 [Note] InnoDB: Shutdown completed; log sequence number 375803935; transaction id 424
db_1     | 2019-02-17  3:23:37 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
db_1     | 2019-02-17  3:23:37 0 [Note] mysqld: Shutdown complete
db_1     |
db_1     |
db_1     | MySQL init process done. Ready for start up.
db_1     |
db_1     | 2019-02-17  3:23:38 0 [Note] mysqld (mysqld 10.4.2-MariaDB-1:10.4.2+maria~bionic) starting as process 1 ...
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Using Linux native AIO
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Uses event mutexes
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Number of pools: 1
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Using SSE2 crc32 instructions
db_1     | 2019-02-17  3:23:38 0 [Note] mysqld: O_TMPFILE is not supported on /tmp (disabling future attempts)
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Initializing buffer pool, total size = 256M, instances = 1, chunk size = 128M
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Completed initialization of buffer pool
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: 128 out of 128 rollback segments are active.
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Creating shared tablespace for temporary tables
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Waiting for purge to start
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: 10.4.2 started; log sequence number 375803935; transaction id 427
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
db_1     | 2019-02-17  3:23:38 0 [Note] Plugin 'FEEDBACK' is disabled.
db_1     | 2019-02-17  3:23:38 0 [Note] Server socket created on IP: '::'.
db_1     | 2019-02-17  3:23:38 0 [Warning] 'proxies_priv' entry '@% root@1008b30fb58f' ignored in --skip-name-resolve mode.
db_1     | 2019-02-17  3:23:38 0 [Note] Reading of all Master_info entries succeded
db_1     | 2019-02-17  3:23:38 0 [Note] Added new Master_info '' to hash table
db_1     | 2019-02-17  3:23:38 0 [Note] mysqld: ready for connections.
db_1     | Version: '10.4.2-MariaDB-1:10.4.2+maria~bionic'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
db_1     | 2019-02-17  3:23:38 0 [Note] InnoDB: Buffer pool(s) load completed at 190217  3:23:38
db_1     | 2019-02-17  3:23:55 8 [Warning] Aborted connection 8 to db: 'employees' user: 'interview_challenge' host: '172.18.0.2' (Got an error reading communication packets)
nginx_1  | 172.18.0.1 - - [17/Feb/2019:03:23:55 +0000] "GET /employees/custom_list HTTP/1.1" 200 8874142 "-" "curl/7.38.0" "-"
```


```
$ curl localhost:8080/employees/custom_list > /dev/null
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8666k  100 8666k    0     0  3862k      0  0:00:02  0:00:02 --:--:-- 3863k
```

### Screenshot

Sample output:

![](https://i.imgur.com/3J9JAjF.png)


## Example using local image

If you want to modify the app behavior you can build locally its docker image.
First you should install docker and docker-compose and then follow this steps:

1. Edit docker-compose.yml

Uncomment the build line:

```
    image: juanchimienti/interview_challeng_app:0.1.1
#    build: .
    environment:
```
2. Modify app.py

Make the changes you wish

3. Rebuild the image

Using the following command:

```
docker-compose build
```

Then docker-compose up to start all again

**Beware: this process will replace the local app docker image.**

