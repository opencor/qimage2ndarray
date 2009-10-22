import qimageview
from PyQt4 import QtGui

from nose.tools import raises, assert_equal

def test_viewcreation():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_RGB32)
	v = qimageview.qimageview(qimg)
	assert_equal(v.shape, (240, 320))

@raises(TypeError)
def test_qimageview_noargs():
	v = qimageview.qimageview()

@raises(TypeError)
def test_qimageview_manyargs():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_Indexed8)
	v = qimageview.qimageview(qimg, 1)

@raises(TypeError)
def test_qimageview_wrongarg():
	v = qimageview.qimageview(42)

def test_data_access():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_Indexed8)
	qimg.setNumColors(256)
	qimg.fill(42)
	v = qimageview.qimageview(qimg)
	assert_equal(v.shape, (240, 320))
	assert_equal(v[10,10], 42)
	assert_equal(v.nbytes, qimg.numBytes())

def test_being_view():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_Indexed8)
	qimg.setNumColors(256)
	qimg.fill(23)
	v = qimageview.qimageview(qimg)
	qimg.fill(42)
	assert_equal(v.shape, (240, 320))
	assert_equal(v[10,10], 42)
	assert_equal(v.nbytes, qimg.numBytes())

def test_coordinate_access():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_Indexed8)
	qimg.setNumColors(256)
	qimg.fill(0)
	qimg.setPixel(12, 10, 42)
	v = qimageview.qimageview(qimg)
	qimg.fill(42)
	assert_equal(v.shape, (240, 320))
	assert_equal(v[10,12], 42)
	assert_equal(v.nbytes, qimg.numBytes())

def test_RGB32():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_RGB32)
	qimg.fill(0)
	qimg.setPixel(12, 10, 42)
	v = qimageview.qimageview(qimg)
	qimg.fill(42)
	assert_equal(v.shape, (240, 320))
	assert_equal(v[10,12], 42 | 0xff000000)
	assert_equal(v.nbytes, qimg.numBytes())

def test_ARGB32():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_ARGB32)
	qimg.fill(0)
	qimg.setPixel(12, 10, 42)
	v = qimageview.qimageview(qimg)
	qimg.fill(42)
	assert_equal(v.shape, (240, 320))
	assert_equal(v[10,12], 42)
	assert_equal(v.nbytes, qimg.numBytes())

@raises(ValueError)
def test_mono():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_Mono)
	v = qimageview.qimageview(qimg)

@raises(ValueError)
def test_rgb666():
	qimg = QtGui.QImage(320, 240, QtGui.QImage.Format_RGB666)
	v = qimageview.qimageview(qimg)
