# TI-84 Plus CE Python programs

A collection of (small) Python programs for the Texas Instruments TI-84 Plus CE Python Edition.
Nothing too **shocking**, since it runs standard Python and most of the usual modules just work.
For a calculator, the most useful one is of course the *math* module.

## Programs

| Program | Description |
|---------|-------------|
| `afstand.py` | Great-circle distance (haversine) in kilometres between two coordinates that are hard-coded in the script. |
| `bmi.py` | Asks for weight (kg) and height (m) and calculates the Body Mass Index. |
| `dhc2.py` | Menu-driven weight & balance calculator for the DHC-2 Beaver: fuel load per tank (USG, Imp. gal or litres, optional tip tanks), cabin load, aircraft settings and a W&B report with CG check. Uses `ti_system`. **Note:** the limits and arms are placeholder values — replace them with the figures from the POH before use. |
| `gc-crs.py` | Asks for two coordinates and calculates the initial and final great-circle course (true heading). |
| `gc-dist.py` | Asks for two coordinates and calculates the great-circle distance in kilometres. |
| `getgdist.py` | Great-circle distance from coordinates stored in a dictionary; also shows the data as JSON (test of the `json` module). |
| `GRAPH.py` | Plots two functions, f(x) = 3x² − 0.4 and g(x) = −f(x), with `ti_plotlib`. Press [clear] to return to the shell. |
| `inhoud-cylinder.py` | Asks for radius and height and calculates the volume of a cylinder. |
| `LINREGR.py` | Ohm's law example: scatter plot of current vs. voltage measurements with a linear regression line (`ti_plotlib`), then prints the coefficients a and b. |
| `ti84-hello.py` | "Hello World": asks for your name and two numbers, then prints a² + b². |
| `ti84-math.py` | Demonstrates built-in math functions (`abs`, `min`, `max`, `pow`) and the `math` module (`sqrt`, `pi`). |
| `varfmt.py` | Experiment with passing a variable column width to `str.format()`. |

Note: the prompts and output of most programs are in Dutch.
