RUN_XEB="python nm_run.py"
RUN_AUX="./aux"
RUN_DEN="./zed"

eval $RUN_XEB &>> "CONSOLE.txt"
eval $RUN_AUX &>> "CONSOLE.txt"
eval $RUN_DEN &>> "CONSOLE.txt"

exit 0
