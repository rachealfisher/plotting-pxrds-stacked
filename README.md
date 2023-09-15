# plotting-pxrds-stacked
For use with XRD data

## Usage

You can use this code to plot two different PXRD plots on each other. It is setup to plot two between 0,25 on the x-axis, but you can change this. This will only work with PXRDs in their original formats. If you want to plot a simulated PXRD file, use `Simulationtocorrectformat.py`. This code assumes that you start with a headerless .txt file with tabs in between the values. This format can be generated using CrystalDiffract software.
Once you have two PXRD files in the format of `PXRDfiletobereplaced`, you can plot them. There is an option to add the scherrer size to the plot, which can be calculated in my `pxrd-scherreranalysis-multipeak-plotting` repository if unknown.

## Output
This code will output one figure with 2 plots stacked on each other. The title and subtitle are customizable. A scherrer size value may be added to the top right in a box. 

## Errors
Make sure that your file is in the correct format if you get any errors. Otherwise, let me know and I will fix :)