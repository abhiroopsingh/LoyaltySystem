
class PrintLogger(object):
    def info(st, *args):
        print "INFO: "+st.format(*args)

    def warn(st, *args):
        print "WARN: "+st.format(*args)

    def err(st, *args):
        print "ERR: "+st.format(*args)

class DiscardLogger(object):
    def info(st, *args):
        pass
    def warn(st, *args):
        pass
    def err(st, *args):
        pass
