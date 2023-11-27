# Stable Baselines3 Class Diagrams

```mermaid
    nnModule <|-- BaseModel
    nnModule <|-- BaseFeaturesExtractor
    nnModule <|-- MlpExtractor

    BaseModel <|-- BasePolicy
    ABC <|-- BasePolicy

    BasePolicy <|-- ActorCriticPolicy
    BasePolicy <|-- QNetwork
    BasePolicy <|-- DQNPolicy
    BasePolicy <|-- Actor
    BasePolicy <|-- SACPolicy
    BasePolicy <|-- ActorCriticPolicy
    BasePolicy <|-- TD3Policy

    DQNPolicy <|-- MultiInputPolicy1
    SACPolicy <|-- MultiInputPolicy2
    TD3Policy <|-- MultiInputPolicy3

    class ActorCriticPolicy{

    }
  
    class BasePolicy{

    }
  
    class BaseFeaturesExtractor{
 
    }

    class BaseModel{

    }

    class nnModule{

    }

    class MlpExtractor {

    }

    class ABC {

    }

```
