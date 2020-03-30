RUN_XEB="python nm_run.py"
RUN_AUX="./aux"

eval $RUN_XEB &>> "CONSOLE.txt"
eval $RUN_AUX &>> "CONSOLE.txt"

exit 0
