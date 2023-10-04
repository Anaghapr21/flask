from masrshmallow import schema,fields
class PlainItemSchema (Schema):
	id=fields.Str(dump_only=True)
	name=fields.Str(required=True)
	price=fields.Float(required=True)



class PlainStoresSchema(schema):
	id=fields.Str(dumo_only=True)
	name=fields.Str(required=True)


class ItemUpdateSchema(schema):
	name=fields.str()
	price=fields.Float()

class ItemSchema(PlainItemSchema):
	store_id=fields.INt(required=True,load_only=True)
	store=fields.Nested(PlainStoreSchema(),dump_only=True)

class StoreSchema(PlainStoreSchema):
	items=fields.LIst(fields.Nested(PLainItemSchema()),dump_only=True)
