imp = IJ.getImage();
rm = RoiManager.getRoiManager();
#IJ.setTool("oval");
imp.setRoi(OvalRoi(36,39,26,28));
roi = imp.getRoi();
roi.setPosition(2, 57, 1);
rm.addRoi(roi);
imp.setRoi(OvalRoi(136,41,38,37));
roi = imp.getRoi();
roi.setPosition(2, 57, 1);
rm.addRoi(roi);
imp.setRoi(OvalRoi(75,160,58,47));
roi = imp.getRoi();
roi.setPosition(2, 57, 1);
rm.addRoi(roi);
imp.setRoi(OvalRoi(191,155,49,52));
roi = imp.getRoi();
roi.setPosition(2, 57, 1);
rm.addRoi(roi);
