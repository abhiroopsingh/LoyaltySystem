
class PrintLogger(object):
    def info(self, st, *args):
        print "INFO: "+st.format(*args)

    def warn(self,st, *args):
        print "WARN: "+st.format(*args)

    def err(self,st, *args):
        print "ERR: "+st.format(*args)

class DiscardLogger(object):
    def info(self,st, *args):
        pass
    def warn(self,st, *args):
        pass
    def err(self,st, *args):
        pass
