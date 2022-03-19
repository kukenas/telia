# Coding Challenge - Path Reduction

### 1 Background

<div style="text-align: justify"> We are given paths to go from one point to another. The paths are "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going one path and coming back the opposite path is a wasted effort, so let us concise these paths to go the shortest route.
For example, given the following paths:
You can immediately see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place!
So the task is to reduce a simplified version of the plan. A better plan in this case is simply:
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the path "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing. The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] .
In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite, but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].</div>

### 2 Task

<div style="text-align: justify"> You have to write a function pathReduc in Python or Scala which will take an array of strings and returns an array of strings with the needless paths removed (W<->E or S<->N side by side).
The task will not only be assessed on correct functionality but also how optimal the code is from a performance perspective.</div>

### 3 Specification

<code><b>TeliaChallenge.pathReduc(arr)</b></code>

<code><b>Parameters</b></code>

<div style="margin-left: 30px;"><code>arr: Array&lt;String&gt; An array with each index containing 1 of the 4 cardinal paths, all in uppercase</code></div>

<code><b>Return Value</b></code>

<div style="margin-left: 30px;"><code>Array&lt;String&gt; - The optimized set of instructions</code></div>

<code><b>Examples</b></code>

<b>arr</b>

<code>["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"]</code>

<code>["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]</code>

<code>["NORTH","WEST","SOUTH","EAST"]</code>

### 4 Note

<div style="text-align: justify">Not all paths can be made simpler.
The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence, the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].</div>

# <ins>Solution:</ins>

1) docker build -t exercise . --progress=plain --no-cache
2) docker run -it exercise bash
3) python3 main.py $(path)

Replace $(path) with the list to be made simpler: <br>
*python3 main.py ["NORTH", "WEST", "SOUTH", "EAST"]*
