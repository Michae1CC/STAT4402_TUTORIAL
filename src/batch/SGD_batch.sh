#!/bin/bash
#SBATCH --job-name=SGD_demo
#SBATCH --output=/home/s4430291/STAT4402_tut/batch_out/SGD_demo4.out
#SBATCH --error=/home/s4430291/STAT4402_tut/batch_out/SGD_demo.err
#SBATCH --time=0-0:10
#SBATCH --mem=1GB
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4

export OMP_NUM_THREADS=4

DATE=$(date +"%Y%m%d%H%M")
echo "time started  "$DATE
echo "This is job '$SLURM_JOB_NAME' (id: $SLURM_JOB_ID) running on the following nodes:"
echo $SLURM_NODELIST
echo "running with SLURM_TASKS_PER_NODE= $SLURM_TASKS_PER_NODE "
echo "running with SLURM_NTASKS total  = $SLURM_NTASKS "
export TIMEFORMAT="%E sec"

python3.6 /home/s4430291/STAT4402_tut/SGD_demo.py -t 4

DATE=$(date +"%Y%m%d%H%M")
echo "time finished "$DATE