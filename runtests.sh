#!/bin/zsh -e

echo "Check ./_trial_temp/test.log and the rest of ./_trial_temp/ if anything fails."
trial test_monoclock

echo
echo "Now running with the Python test runner..."
python -W all -m unittest test_monoclock
