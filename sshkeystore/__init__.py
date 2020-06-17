from . import store
from .agent import Agent, AgentError
from .keys import KeyLoadError


def cli():
    try:
        pubstore = store.PubdirStore.get_default_store()
    except Exception as e:
        pubstore = None
        print(f"Error getting PubdirStore: {e}")
    for kp in store.Keystore.get_default_store():
        try:
            Agent.addkey(kp.private())
        except AgentError as e:
            print(f"Error adding key '{kp.name}' to agent: {e}")
        except KeyLoadError as e:
            print(f"Error loading key '{kp.name}': {e}")
        else:
            print(f"Added '{kp.name}'")
            try:
                if pubstore:
                    pubstore.add(kp.name, kp.public())
            except KeyLoadError as e:
                print(f"Error loading public key for '{kp.name}': {e}")
