if [ $# -lt 3 ]
then
  echo "Use: <train_dir> <test_dir> <number_to_move>"
  exit 1
fi

ls -Q -S $1 | head -$3 | xargs -i mv $1{} $2
