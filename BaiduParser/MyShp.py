import shapefile
import json

def read_shp(path):
    json_path = 'GeoJson.json'

    reader = shapefile.Reader(path, encoding='gbk') #你他妈的
    record = reader.record(0)
    shape_record = reader.shapeRecord(0)
    print(reader.shape(0).shapeType)

    shapefile.POLYGON
    print(record)
    print(shape_record.__geo_interface__)
    # print(reader.fields)

    # print(len(records))
    # print(len(fields))
    # json.dump()

    # with open(json_path, mode='w') as fp:
    #     fp.write()
    # reader = shapefile.Reader(path)
    # for i in range(len(reader)):
    #     cur_shape = reader.shape(i)
    #
    #     if(len(cur_shape.parts) != 1):
    #         print(cur_shape)
    #         print(cur_shape.parts)
    #     # print(cur_shape)
        # print(cur_shape.parts)

