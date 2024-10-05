import ultralytics


from roboflow import Roboflow
rf = Roboflow(api_key="2u1E4EsIRlyUkGb2N6bh")
project = rf.workspace("object-detction-oewxm").project("object-detection-jhizg")
version = project.version(1)
dataset = version.download("yolov8")
                