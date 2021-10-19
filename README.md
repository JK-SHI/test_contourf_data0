# test_contourf_data0
Sample Program to show that Data 0 cannot be plotted by matplotlib.pyplot(3.3.4) just because some data is less than 0 (python 3.8.8).
the left-bottom area in the right figure is not colored and remains transparent just because some data are changed to -1.7E-13.
(see attached png file contourf_jet4r.png.)


