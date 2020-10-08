#!/bin/bash
#SBATCH --job-name=PERCEPTRON_demo
#SBATCH --output=/home/s4430291/STAT4402_tut/batch_out/PERCEPTRON_demo.out
#SBATCH --error=/home/s4430291/STAT4402_tut/batch_out/PERCEPTRON_demo.err
#SBATCH --time=0-0:05
#SBATCH --mem=1GB
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1

export OMP_NUM_THREADS=1

DATE=$(date +"%Y%m%d%H%M")
echo "time started  "$DATE
echo "This is job '$SLURM_JOB_NAME' (id: $SLURM_JOB_ID) running on the following nodes:"
echo $SLURM_NODELIST
echo "running with SLURM_TASKS_PER_NODE= $SLURM_TASKS_PER_NODE "
echo "running with SLURM_NTASKS total  = $SLURM_NTASKS "
export TIMEFORMAT="%E sec"

python3 /home/s4430291/STAT4402_tut/PERCEPTRON_demo.py

DATE=$(date +"%Y%m%d%H%M")
echo "time finished "$DATE
