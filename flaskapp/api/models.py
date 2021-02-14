from flaskapp import db

class G44(db.Model):
    __tablename__ = 'g44'
    __table_args__ = {'extend_existing': True}

    LFSFF_C16 = db.Column(db.String(100))
    Labour_force_status_Female = db.Column(db.String(100))
    LFSMF_C16 = db.Column(db.String(100))
    Labour_force_status_Male = db.Column(db.String(100))
    ASGS_2016 = db.Column(db.Integer)
    region = db.Column(db.String(100))
    value = db.Column(db.Integer)

class G45(db.Model):
    __tablename__ = 'g45'
    __table_args__ = {'extend_existing': True}

    Sex = db.Column(db.String(100))
    LFSP_C16 = db.Column(db.String(100))
    Labour_force_status = db.Column(db.String(100))
    ASGS_2016 = db.Column(db.Integer)
    region = db.Column(db.String(100))
    value = db.Column(db.Integer)


class Communication(db.Model):
    __tablename__ = 'communication'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    on_track = db.Column(db.Integer)
    at_risk = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)


class Social(db.Model):
    __tablename__ = 'social'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    on_track = db.Column(db.Integer)
    at_risk = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)
  
class Emotional(db.Model):
    __tablename__ = 'emotional'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    on_track = db.Column(db.Integer)
    at_risk = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)

class Language(db.Model):
    __tablename__ = 'language'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    on_track = db.Column(db.Integer)
    at_risk = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)

class Health(db.Model):
    __tablename__ = 'health'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    on_track = db.Column(db.Integer)
    at_risk = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)

class Oneormore(db.Model):
    __tablename__ = 'oneormore'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)


class Twoormore(db.Model):
    __tablename__ = 'twoormore'
    __table_args__ = {'extend_existing': True}

    code = db.Column(db.String(10))
    name = db.Column(db.String(100))
    total = db.Column(db.Integer)
    vulnerable = db.Column(db.Integer)
    vulnerable_percentage = db.Column(db.Float)