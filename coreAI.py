from coreai.ai.rule_based_ai import RuleBasedAI
from coreai.environment.simulator import GameSimulator
from coreai.utils.logger import setup_logger

def main():
    # Set up logging
    logger = setup_logger()

    # Initialize the game environment
    simulator = GameSimulator(level_file="assets/levels/level1.json")
    game_state = simulator.reset()

    # Initialize the AI
    ai = RuleBasedAI()

    # Run the AI
    while not game_state.is_game_over():
        action = ai.decide_action(game_state)
        game_state = simulator.step(action)
        logger.info(f"Action: {action}, State: {game_state}")

if __name__ == "__main__":
    main()