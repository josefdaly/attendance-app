import datetime

from marshmallow import Schema, fields


class RecurringScheduledSessionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    day = fields.Function(lambda obj: obj.get_day_display())
    time = fields.DateTime()
    date = fields.Method('get_date')

    def get_date(self, obj):
        today = datetime.date.today()
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            new_date = today + datetime.timedelta(days=i)
            if new_date.strftime('%A') == obj.get_day_display():
                return new_date.strftime("%m/%d/%Y")


class OneTimeScheduledSessionSchema(RecurringScheduledSessionSchema):
    date = fields.Function(lambda obj: obj.date.strftime("%m/%d/%Y"))
    day = fields.Function(lambda obj: obj.date.strftime("%A"))
