Started by user kashish tiwari
Running as SYSTEM
Building in workspace C:\Users\DELL\.jenkins\workspace\nopcommerce_selenium_python_project
The recommended git tool is: NONE
No credentials specified
Cloning the remote Git repository
Cloning repository https://github.com/kash-ish2/nopcommerce.git
 > C:\Program Files\Git\bin\git.exe init C:\Users\DELL\.jenkins\workspace\nopcommerce_selenium_python_project # timeout=10
Fetching upstream changes from https://github.com/kash-ish2/nopcommerce.git
 > C:\Program Files\Git\bin\git.exe --version # timeout=10
 > git --version # 'git version 2.53.0.windows.1'
 > C:\Program Files\Git\bin\git.exe fetch --tags --force --progress -- https://github.com/kash-ish2/nopcommerce.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > C:\Program Files\Git\bin\git.exe config remote.origin.url https://github.com/kash-ish2/nopcommerce.git # timeout=10
 > C:\Program Files\Git\bin\git.exe config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > C:\Program Files\Git\bin\git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
Checking out Revision d8bd1bc3addff5fdf95221c603f92d996ce9d505 (refs/remotes/origin/master)
 > C:\Program Files\Git\bin\git.exe config core.sparsecheckout # timeout=10
 > C:\Program Files\Git\bin\git.exe checkout -f d8bd1bc3addff5fdf95221c603f92d996ce9d505 # timeout=10
Commit message: "added run.bat"
First time build. Skipping changelog.
[nopcommerce_selenium_python_project] $ cmd /c call C:\Users\DELL\AppData\Local\Temp\jenkins11704962612442758851.bat

C:\Users\DELL\.jenkins\workspace\nopcommerce_selenium_python_project>run.bat
'run.bat' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\DELL\.jenkins\workspace\nopcommerce_selenium_python_project>exit 9009
Build step 'Execute Windows batch command' marked build as failure
Finished: FAILURE