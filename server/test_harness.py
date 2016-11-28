import memory_persist as mp
import notification_system
import data
import demo_data
import log


def setup():
    db = mp.MemoryPersist()
    demo_data.add_demo_data(db)
    logger = log.DiscardLogger()
    notifier = notification_system.NotificationServer()
    return (db, logger, notifier)

