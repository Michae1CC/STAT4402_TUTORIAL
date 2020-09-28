#!/bin/bash
#SBATCH --job-name=InverseSolver
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

python3 /home/s4430291/Courses/MATH3204/MATH3204_A2/src/Q4_main.py InverseSolver

DATE=$(date +"%Y%m%d%H%M")
echo "time finished "$DATE
