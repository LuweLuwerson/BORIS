# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prefDialog(object):
    def setupUi(self, prefDialog):
        prefDialog.setObjectName("prefDialog")
        prefDialog.setWindowModality(QtCore.Qt.WindowModal)
        prefDialog.resize(596, 588)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(prefDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(prefDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cbTimeFormat = QtWidgets.QComboBox(self.tab)
        self.cbTimeFormat.setObjectName("cbTimeFormat")
        self.cbTimeFormat.addItem("")
        self.cbTimeFormat.addItem("")
        self.gridLayout.addWidget(self.cbTimeFormat, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.sbffSpeed = QtWidgets.QSpinBox(self.tab)
        self.sbffSpeed.setMinimum(0)
        self.sbffSpeed.setMaximum(10000)
        self.sbffSpeed.setProperty("value", 10)
        self.sbffSpeed.setObjectName("sbffSpeed")
        self.gridLayout.addWidget(self.sbffSpeed, 1, 1, 1, 1)
        self.cb_adapt_fast_jump = QtWidgets.QCheckBox(self.tab)
        self.cb_adapt_fast_jump.setObjectName("cb_adapt_fast_jump")
        self.gridLayout.addWidget(self.cb_adapt_fast_jump, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.sbRepositionTimeOffset = QtWidgets.QSpinBox(self.tab)
        self.sbRepositionTimeOffset.setMinimum(-10000)
        self.sbRepositionTimeOffset.setMaximum(10000)
        self.sbRepositionTimeOffset.setProperty("value", -3)
        self.sbRepositionTimeOffset.setObjectName("sbRepositionTimeOffset")
        self.gridLayout.addWidget(self.sbRepositionTimeOffset, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.sbSpeedStep = QtWidgets.QDoubleSpinBox(self.tab)
        self.sbSpeedStep.setDecimals(1)
        self.sbSpeedStep.setMinimum(0.1)
        self.sbSpeedStep.setMaximum(1.0)
        self.sbSpeedStep.setSingleStep(0.1)
        self.sbSpeedStep.setProperty("value", 0.1)
        self.sbSpeedStep.setObjectName("sbSpeedStep")
        self.gridLayout.addWidget(self.sbSpeedStep, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.sbAutomaticBackup = QtWidgets.QSpinBox(self.tab)
        self.sbAutomaticBackup.setMinimum(-10000)
        self.sbAutomaticBackup.setMaximum(10000)
        self.sbAutomaticBackup.setProperty("value", 10)
        self.sbAutomaticBackup.setObjectName("sbAutomaticBackup")
        self.gridLayout.addWidget(self.sbAutomaticBackup, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.leSeparator = QtWidgets.QLineEdit(self.tab)
        self.leSeparator.setObjectName("leSeparator")
        self.gridLayout.addWidget(self.leSeparator, 6, 1, 1, 1)
        self.cbCloseSameEvent = QtWidgets.QCheckBox(self.tab)
        self.cbCloseSameEvent.setObjectName("cbCloseSameEvent")
        self.gridLayout.addWidget(self.cbCloseSameEvent, 7, 0, 1, 1)
        self.cbConfirmSound = QtWidgets.QCheckBox(self.tab)
        self.cbConfirmSound.setObjectName("cbConfirmSound")
        self.gridLayout.addWidget(self.cbConfirmSound, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.sbBeepEvery = QtWidgets.QSpinBox(self.tab)
        self.sbBeepEvery.setObjectName("sbBeepEvery")
        self.gridLayout.addWidget(self.sbBeepEvery, 9, 1, 1, 1)
        self.cbAlertNoFocalSubject = QtWidgets.QCheckBox(self.tab)
        self.cbAlertNoFocalSubject.setObjectName("cbAlertNoFocalSubject")
        self.gridLayout.addWidget(self.cbAlertNoFocalSubject, 10, 0, 1, 1)
        self.cbTrackingCursorAboveEvent = QtWidgets.QCheckBox(self.tab)
        self.cbTrackingCursorAboveEvent.setObjectName("cbTrackingCursorAboveEvent")
        self.gridLayout.addWidget(self.cbTrackingCursorAboveEvent, 11, 0, 1, 1)
        self.cbCheckForNewVersion = QtWidgets.QCheckBox(self.tab)
        self.cbCheckForNewVersion.setObjectName("cbCheckForNewVersion")
        self.gridLayout.addWidget(self.cbCheckForNewVersion, 12, 0, 1, 1)
        self.cb_display_subtitles = QtWidgets.QCheckBox(self.tab)
        self.cb_display_subtitles.setObjectName("cb_display_subtitles")
        self.gridLayout.addWidget(self.cb_display_subtitles, 13, 0, 1, 1)
        self.cb_pause_before_addevent = QtWidgets.QCheckBox(self.tab)
        self.cb_pause_before_addevent.setObjectName("cb_pause_before_addevent")
        self.gridLayout.addWidget(self.cb_pause_before_addevent, 14, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbFFmpegPath = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegPath.setScaledContents(False)
        self.lbFFmpegPath.setWordWrap(True)
        self.lbFFmpegPath.setObjectName("lbFFmpegPath")
        self.verticalLayout_3.addWidget(self.lbFFmpegPath)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbFFmpegCacheDir = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegCacheDir.setObjectName("lbFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.lbFFmpegCacheDir)
        self.leFFmpegCacheDir = QtWidgets.QLineEdit(self.tab_2)
        self.leFFmpegCacheDir.setObjectName("leFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.leFFmpegCacheDir)
        self.pbBrowseFFmpegCacheDir = QtWidgets.QPushButton(self.tab_2)
        self.pbBrowseFFmpegCacheDir.setObjectName("pbBrowseFFmpegCacheDir")
        self.horizontalLayout_3.addWidget(self.pbBrowseFFmpegCacheDir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbFFmpegCacheDirMaxSize = QtWidgets.QLabel(self.tab_2)
        self.lbFFmpegCacheDirMaxSize.setObjectName("lbFFmpegCacheDirMaxSize")
        self.horizontalLayout_4.addWidget(self.lbFFmpegCacheDirMaxSize)
        self.sbFFmpegCacheDirMaxSize = QtWidgets.QSpinBox(self.tab_2)
        self.sbFFmpegCacheDirMaxSize.setMaximum(10000)
        self.sbFFmpegCacheDirMaxSize.setSingleStep(10)
        self.sbFFmpegCacheDirMaxSize.setObjectName("sbFFmpegCacheDirMaxSize")
        self.horizontalLayout_4.addWidget(self.sbFFmpegCacheDirMaxSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lb_cache_size = QtWidgets.QLabel(self.tab_3)
        self.lb_cache_size.setEnabled(True)
        self.lb_cache_size.setObjectName("lb_cache_size")
        self.horizontalLayout_9.addWidget(self.lb_cache_size)
        self.sb_fbf_cache_size = QtWidgets.QSpinBox(self.tab_3)
        self.sb_fbf_cache_size.setEnabled(True)
        self.sb_fbf_cache_size.setMinimum(1)
        self.sb_fbf_cache_size.setMaximum(3600)
        self.sb_fbf_cache_size.setObjectName("sb_fbf_cache_size")
        self.horizontalLayout_9.addWidget(self.sb_fbf_cache_size)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_resize_frame = QtWidgets.QLabel(self.tab_3)
        self.lb_resize_frame.setEnabled(True)
        self.lb_resize_frame.setWordWrap(True)
        self.lb_resize_frame.setObjectName("lb_resize_frame")
        self.horizontalLayout_5.addWidget(self.lb_resize_frame)
        self.sbFrameResize = QtWidgets.QSpinBox(self.tab_3)
        self.sbFrameResize.setEnabled(True)
        self.sbFrameResize.setMaximum(1920)
        self.sbFrameResize.setSingleStep(10)
        self.sbFrameResize.setObjectName("sbFrameResize")
        self.horizontalLayout_5.addWidget(self.sbFrameResize)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.rb_save_frames_in_mem = QtWidgets.QRadioButton(self.tab_3)
        self.rb_save_frames_in_mem.setEnabled(False)
        self.rb_save_frames_in_mem.setChecked(True)
        self.rb_save_frames_in_mem.setObjectName("rb_save_frames_in_mem")
        self.verticalLayout_6.addWidget(self.rb_save_frames_in_mem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lb_memory_frames = QtWidgets.QLabel(self.tab_3)
        self.lb_memory_frames.setEnabled(False)
        self.lb_memory_frames.setObjectName("lb_memory_frames")
        self.horizontalLayout_6.addWidget(self.lb_memory_frames)
        self.sb_frames_memory_size = QtWidgets.QSpinBox(self.tab_3)
        self.sb_frames_memory_size.setEnabled(False)
        self.sb_frames_memory_size.setMinimum(5)
        self.sb_frames_memory_size.setMaximum(100)
        self.sb_frames_memory_size.setSingleStep(5)
        self.sb_frames_memory_size.setProperty("value", 80)
        self.sb_frames_memory_size.setObjectName("sb_frames_memory_size")
        self.horizontalLayout_6.addWidget(self.sb_frames_memory_size)
        self.lb_percent_total_memory = QtWidgets.QLabel(self.tab_3)
        self.lb_percent_total_memory.setEnabled(False)
        self.lb_percent_total_memory.setObjectName("lb_percent_total_memory")
        self.horizontalLayout_6.addWidget(self.lb_percent_total_memory)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.lb_memory_in_use = QtWidgets.QLabel(self.tab_3)
        self.lb_memory_in_use.setEnabled(False)
        self.lb_memory_in_use.setObjectName("lb_memory_in_use")
        self.verticalLayout_6.addWidget(self.lb_memory_in_use)
        self.rb_save_frames_on_disk = QtWidgets.QRadioButton(self.tab_3)
        self.rb_save_frames_on_disk.setObjectName("rb_save_frames_on_disk")
        self.verticalLayout_6.addWidget(self.rb_save_frames_on_disk)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lb_bitmap_quality = QtWidgets.QLabel(self.tab_3)
        self.lb_bitmap_quality.setEnabled(False)
        self.lb_bitmap_quality.setObjectName("lb_bitmap_quality")
        self.horizontalLayout_8.addWidget(self.lb_bitmap_quality)
        self.cbFrameBitmapFormat = QtWidgets.QComboBox(self.tab_3)
        self.cbFrameBitmapFormat.setEnabled(False)
        self.cbFrameBitmapFormat.setObjectName("cbFrameBitmapFormat")
        self.cbFrameBitmapFormat.addItem("")
        self.cbFrameBitmapFormat.addItem("")
        self.horizontalLayout_8.addWidget(self.cbFrameBitmapFormat)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.lb_storage_dir = QtWidgets.QLabel(self.tab_3)
        self.lb_storage_dir.setEnabled(False)
        self.lb_storage_dir.setObjectName("lb_storage_dir")
        self.verticalLayout_6.addWidget(self.lb_storage_dir)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.cbSpectrogramColorMap = QtWidgets.QComboBox(self.tab_4)
        self.cbSpectrogramColorMap.setObjectName("cbSpectrogramColorMap")
        self.horizontalLayout_7.addWidget(self.cbSpectrogramColorMap)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.sb_time_interval = QtWidgets.QSpinBox(self.tab_4)
        self.sb_time_interval.setMinimum(2)
        self.sb_time_interval.setMaximum(360)
        self.sb_time_interval.setProperty("value", 10)
        self.sb_time_interval.setObjectName("sb_time_interval")
        self.horizontalLayout_10.addWidget(self.sb_time_interval)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 319, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.te_plot_colors = QtWidgets.QPlainTextEdit(self.tab_5)
        self.te_plot_colors.setObjectName("te_plot_colors")
        self.verticalLayout_10.addWidget(self.te_plot_colors)
        self.pb_reset_colors = QtWidgets.QPushButton(self.tab_5)
        self.pb_reset_colors.setObjectName("pb_reset_colors")
        self.verticalLayout_10.addWidget(self.pb_reset_colors)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pb_refresh = QtWidgets.QPushButton(prefDialog)
        self.pb_refresh.setObjectName("pb_refresh")
        self.horizontalLayout_2.addWidget(self.pb_refresh)
        self.pbCancel = QtWidgets.QPushButton(prefDialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(prefDialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(prefDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(prefDialog)

    def retranslateUi(self, prefDialog):
        _translate = QtCore.QCoreApplication.translate
        prefDialog.setWindowTitle(_translate("prefDialog", "Preferences"))
        self.label.setText(_translate("prefDialog", "Default project time format"))
        self.cbTimeFormat.setItemText(0, _translate("prefDialog", "seconds"))
        self.cbTimeFormat.setItemText(1, _translate("prefDialog", "hh:mm:ss.mss"))
        self.label_4.setText(_translate("prefDialog", "Fast forward/backward speed (seconds)"))
        self.cb_adapt_fast_jump.setText(_translate("prefDialog", "Adapt the fast forward/backward jump to playback speed"))
        self.label_2.setText(_translate("prefDialog", "Time offset for video/audio reposition (seconds)"))
        self.label_5.setText(_translate("prefDialog", "Playback speed step value"))
        self.label_6.setText(_translate("prefDialog", "Auto-save project every (minutes)"))
        self.label_3.setText(_translate("prefDialog", "Separator for behavioural strings (events export)"))
        self.leSeparator.setText(_translate("prefDialog", "|"))
        self.cbCloseSameEvent.setText(_translate("prefDialog", "Close the same current event independently of modifiers"))
        self.cbConfirmSound.setText(_translate("prefDialog", "Play sound when a key is pressed"))
        self.label_8.setText(_translate("prefDialog", "Beep every (seconds)"))
        self.cbAlertNoFocalSubject.setText(_translate("prefDialog", "Alert if focal subject is not set"))
        self.cbTrackingCursorAboveEvent.setText(_translate("prefDialog", "Tracking cursor above current event"))
        self.cbCheckForNewVersion.setText(_translate("prefDialog", "Check for new version and news"))
        self.cb_display_subtitles.setText(_translate("prefDialog", "Display subtitles"))
        self.cb_pause_before_addevent.setText(_translate("prefDialog", "Pause media before \"Add event\" command"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("prefDialog", "Project"))
        self.lbFFmpegPath.setText(_translate("prefDialog", "FFmpeg path:"))
        self.lbFFmpegCacheDir.setText(_translate("prefDialog", "FFmpeg cache directory"))
        self.pbBrowseFFmpegCacheDir.setText(_translate("prefDialog", "..."))
        self.lbFFmpegCacheDirMaxSize.setText(_translate("prefDialog", "FFmpeg cache directory max size (Mb)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("prefDialog", "FFmpeg framework"))
        self.lb_cache_size.setText(_translate("prefDialog", "Cache size (in seconds)"))
        self.lb_resize_frame.setText(_translate("prefDialog", "Resize frame (horizontal number of pixels). 0 for no resizing"))
        self.rb_save_frames_in_mem.setText(_translate("prefDialog", "Save frames in memory"))
        self.lb_memory_frames.setText(_translate("prefDialog", "Maximum amount of memory"))
        self.lb_percent_total_memory.setText(_translate("prefDialog", "% of total memory"))
        self.lb_memory_in_use.setText(_translate("prefDialog", "Memory in use"))
        self.rb_save_frames_on_disk.setText(_translate("prefDialog", "Save frames on disk"))
        self.lb_bitmap_quality.setText(_translate("prefDialog", "Frame bitmap format (JPG: Low quality  PNG: High quality)"))
        self.cbFrameBitmapFormat.setItemText(0, _translate("prefDialog", "JPG"))
        self.cbFrameBitmapFormat.setItemText(1, _translate("prefDialog", "PNG"))
        self.lb_storage_dir.setText(_translate("prefDialog", "The cache directory of FFmpeg framework will be used for the frames storage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("prefDialog", "Frame-by-frame mode"))
        self.label_7.setText(_translate("prefDialog", "Color map"))
        self.label_12.setText(_translate("prefDialog", "Default time interval (s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("prefDialog", "Spectrogram"))
        self.label_10.setText(_translate("prefDialog", "List of colors to be used in plot. See <a href=\"https://matplotlib.org/api/colors_api.html\">matplotlib colors</a>"))
        self.pb_reset_colors.setText(_translate("prefDialog", "Reset colors to default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("prefDialog", "Plot colors"))
        self.pb_refresh.setText(_translate("prefDialog", "Refresh"))
        self.pbCancel.setText(_translate("prefDialog", "Cancel"))
        self.pbOK.setText(_translate("prefDialog", "OK"))
