# Old test logs

* in `darkflow_env` and `darkflow` folder, ran `flow --model cfg/yolo.cfg --load bin/yolo.weights --demo camera --gpu 0.5` => OK
* conda installed `numba`, `matplotlib`, `scikit-image`, `scikit-learn`
* pip installed `filterpy`
* ran `python run.py`, returned the following errors:

```
2017-12-18 11:50:49.378305: E tensorflow/stream_executor/cuda/cuda_dnn.cc:371] could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
2017-12-18 11:50:49.378337: E tensorflow/stream_executor/cuda/cuda_dnn.cc:338] could not destroy cudnn handle: CUDNN_STATUS_BAD_PARAM
2017-12-18 11:50:49.378345: F tensorflow/core/kernels/conv_ops.cc:672] Check failed: stream->parent()->GetConvolveAlgorithms( conv_parameters.ShouldIncludeWinogradNonfusedAlgo<T>(), &algorithms) 
Aborted (core dumped)
```
* edited `run.py` and reduced `FLAGS.gpu = 0.7` to `0.5`, then everything was okay. 

## Video test
* downloaded [a test video](https://www.youtube.com/watch?v=R16rluYoeWA)
* trimmed and remove the audio track from the video, saved as `../darkflow/repo/vid_test/test_vid_smash_window.mp4`
* the program show the frames when it was running.
* set `FLAGS.saveVideo=True` but returned the following errors and save no video:


```
OpenCV: FFMPEG: tag 0x44495658/'XVID' is not supported with codec id 13 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x00000020/' ???'

(python:7368): GLib-GObject-CRITICAL **: g_object_set: assertion 'G_IS_OBJECT (object)' failed

** (python:7368): CRITICAL **: gst_app_src_set_caps: assertion 'GST_IS_APP_SRC (appsrc)' failed

** (python:7368): CRITICAL **: gst_app_src_set_stream_type: assertion 'GST_IS_APP_SRC (appsrc)' failed

** (python:7368): CRITICAL **: gst_app_src_set_size: assertion 'GST_IS_APP_SRC (appsrc)' failed

(python:7368): GLib-GObject-CRITICAL **: g_object_set: assertion 'G_IS_OBJECT (object)' failed

(python:7368): GLib-GObject-CRITICAL **: g_object_set: assertion 'G_IS_OBJECT (object)' failed

(python:7368): GLib-GObject-CRITICAL **: g_object_set: assertion 'G_IS_OBJECT (object)' failed

(python:7368): GStreamer-CRITICAL **: gst_bin_add_many: assertion 'GST_IS_ELEMENT (element_1)' failed

(python:7368): GStreamer-CRITICAL **: gst_element_link_many: assertion 'GST_IS_ELEMENT (element_1)' failed
OpenCV Error: Unspecified error (GStreamer: cannot link elements
) in CvVideoWriter_GStreamer::open, file ~/0_sandbox/opencv/modules/videoio/src/cap_gstreamer.cpp, line 1632
VIDEOIO(cvCreateVideoWriter_GStreamer (filename, fourcc, fps, frameSize, is_color)): raised OpenCV exception:

~/0_sandbox/opencv/modules/videoio/src/cap_gstreamer.cpp:1632: error: (-2) GStreamer: cannot link elements
 in function CvVideoWriter_GStreamer::open
```

* convert the input video from mp4 to avi, and got almost the same errors without the following two lines:


```
OpenCV: FFMPEG: tag 0x44495658/'XVID' is not supported with codec id 13 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x00000020/' ???'
```

  * note that the conversion from mp4 to avi will loss considerable quality without some setting.
    The workaround here was to assign the bit-rate to a high value:

    `avconv -i test_vid_smash_window.mp4 -b:v 8000k test_vid_smash_window.avi`

* when setting `FLAGS.csv = True`, there was a csv file contained detected `(frame_id,track_id,x,y,w,h)` data in the same folder containing the input video.
* set `FLAGS.skip = 2` and the processing frame rate went from about 10 fps to 2x fps.
* the `saveVideo` flag went into `darkflow/darkflow/net/help.py`


  ```
  if SaveVideo:
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      if file == 0:#camera window
        fps = 1 / self._get_fps(frame)
        if fps < 1:
          fps = 1
      else:
          fps = round(camera.get(cv2.CAP_PROP_FPS))
      videoWriter = cv2.VideoWriter(
          'output_{}'.format(file), fourcc, fps, (width, height))
  ```

* Copied and saved the sample code of [Getting Started with Videos](https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html) as `repo/check_vid_write.py` and ran it without errors.
* Changed the format of __file name__ as fixed string `output.avi` and the results could be saved as video.
  * The output video has been saved in the folder of `run.py`, and it had been manually moved as `repo/output_sort_person.avi`.
* Printed out the result of `'output_{}'.format(file)` and got `output_../darkflow/repo/vid_test/test_vid_smash_window.avi`.
  The path was obviously problematic.
* TODO
  * Correct the output path of the video
  * Check the output path of the csv file
