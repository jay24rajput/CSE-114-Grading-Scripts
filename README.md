# CSE-114-Grading-Scripts

## Rename Script Steps

1. Download and extract the files from brighspace
2. Place the `rename.py` file in the extracted folder
3. Run the rename script and all the folders will be renamed as per entries in brightspace:<br>
```sh
python3 rename.py
```

## Grading Scripts
1. Download the grading script corresponding to particular assignment/lab
2. Extract the zip file for each student and place the grading script in the directory containing the solution files(like `Solution1.java`, `Solution2.java`, etc)
3. Input the files you want to check similar to : https://github.com/jay24rajput/CSE-114-Grading-Scripts/blob/063a123e0db6f729401fd920d4533fb1b8b6dec4/grade_assignment_1.py#L79
4. Input the arguments for each file similar to:
https://github.com/jay24rajput/CSE-114-Grading-Scripts/blob/063a123e0db6f729401fd920d4533fb1b8b6dec4/grade_assignment_1.py#L80
5. Run the grading script in your terminal:
```python3 <your_grading_script>.py```
6. You should see the stdout of the Java programs

## Note: This is still WIP and for any odd results always run the java code to verify
