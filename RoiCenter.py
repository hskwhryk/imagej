from ij import IJ, ImagePlus;
from ij.plugin.frame import RoiManager;
from ij.process import ImageStatistics as IS;
from ij.gui import PolygonRoi;
from ij.gui import Roi;
from ij.measure import ResultsTable;
from operator import itemgetter, attrgetter;


imp = IJ.getImage();
rm = RoiManager.getRoiManager();
rt = ResultsTable()
# IJ.run("Set Measurements...", "centroid redirect=None decimal=3");
# rm.runCommand(imp,"Measure");
# Create a new list to store the mean intensity values of each blob:
centroids = []
n = 0
 
for roi in RoiManager.getInstance().getRoisAsArray():
  imp.setRoi(roi)
  stats = imp.getStatistics(IS.CENTROID)
  rt.incrementCounter() # Adds a row in Results table
  #rt.addValue adds a value corresponding to column name
  # n = n + 1;
  n = RoiManager.getInstance().getRoiIndex(roi)
  rt.addValue("No.", n)
  rt.addValue("Slice", roi.getTPosition()) 
  rt.addValue("Label", roi.getName())
  rt.addValue("xCentroid", stats.xCentroid);
  rt.addValue("yCentroid", stats.yCentroid);
  spot=roi.getName()
  centroids.append([n, stats.xCentroid, stats.yCentroid])
  # print(centroids)

sortedCentroids = sorted(centroids, key=itemgetter(1))
if (sortedCentroids[0][2] < sortedCentroids[1][2]):
	rm.select(sortedCentroids[0][0]);
	rm.runCommand("Rename", "Top-Left");
	rm.select(sortedCentroids[1][0]);
	rm.runCommand("Rename", "Bottom-Left");
	rm.select(sortedCentroids[2][0]);
	rm.runCommand("Rename", "Top-Right");
	rm.select(sortedCentroids[3][0]);
	rm.runCommand("Rename", "Bottom-Right");
else:
	rm.select(sortedCentroids[0][0]);
	rm.runCommand("Rename", "Bottom-Left");
	rm.select(sortedCentroids[1][0]);
	rm.runCommand("Rename", "Top-Left");
	rm.select(sortedCentroids[2][0]);
	rm.runCommand("Rename", "Bottom-Right");
	rm.select(sortedCentroids[3][0]);
	rm.runCommand("Rename", "Top-Right");
print(sortedCentroids)
rt.show("Center") 