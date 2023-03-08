import shapefile
import json

def read_shp(path):
    # json_path = 'GeoJson.json'
    # print(path)
    # reader = shapefile.Reader(path, encoding='gbk') #你他妈的
    # record = reader.record(0)
    # shape_record = reader.shapeRecord(0)
    # print(reader.shape(0).shapeType)
    #
    # shapefile.POLYGON
    # print(record)
    # print(shape_record.__geo_interface__)

    path = 'D:/Architecture/UrbanGraduation/TestData/上海市/上海市_市区一级道路.shp'
    print(path)
    reader = shapefile.Reader(path, encoding='gbk')  # 你他妈的
    record = reader.record(0)
    shape_record = reader.shapeRecord(0)
    print(reader.shape(0).shapeType)