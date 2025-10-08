const { ModesManager, AIChaosBrain, BeastBestiary, Kate } = require('./game_classes.js');

function run_game_scenario() {
    console.log("--- Initializing Game ---");
    const modes_manager = new ModesManager();
    const ai_brain = new AIChaosBrain(modes_manager);
    const bestiary = new BeastBestiary(modes_manager, 20);
    const player = new Kate();

    console.log(`Welcome, ${player.name}! Your trait: ${player.trait}`);
    console.log(`Initial mode: ${modes_manager.current_mode}`);
    console.log(`Initial difficulty: ${modes_manager.difficulty}`);
    console.log(`Initial coins: ${bestiary.coins}`);
    console.log("-".repeat(20));

    // --- SCENARIO 1: MEDIUM DIFFICULTY (DEFAULT) ---
    console.log("\n--- Scenario: Medium Difficulty ---");
    console.log(`Current difficulty: ${modes_manager.difficulty}`);

    // Demonstrate AI twist
    console.log("\nSimulating player dodging...");
    ai_brain.learn_move('attack');
    ai_brain.learn_move('attack');
    ai_brain.learn_move('dodge');
    console.log("AI response (1 dodge):", ai_brain.throw_twist());
    ai_brain.learn_move('dodge');
    ai_brain.learn_move('dodge');
    console.log("AI response (3 dodges):", ai_brain.throw_twist());

    // Demonstrate beast cost
    console.log("\nAttempting to buy a knight_mount (base cost 10)...");
    console.log(bestiary.buy_beast('knight_mount'));
    console.log(`Coins remaining: ${bestiary.coins}`);
    console.log("-".repeat(20));


    // --- SCENARIO 2: EASY DIFFICULTY ---
    console.log("\n--- Scenario: Easy Difficulty ---");
    modes_manager.set_difficulty('easy');
    console.log(`Difficulty changed to: ${modes_manager.difficulty}`);
    ai_brain.player_moves = []; // Reset moves for a clean test
    bestiary.coins = 20; // Reset coins

    // Demonstrate AI twist (less sensitive)
    console.log("\nSimulating player dodging (less sensitive)...");
    ai_brain.learn_move('dodge');
    console.log("AI response (1 dodge):", ai_brain.throw_twist());
    ai_brain.learn_move('dodge');
    console.log("AI response (2 dodges):", ai_brain.throw_twist());

    // Demonstrate beast cost (cheaper)
    console.log("\nAttempting to buy a knight_mount (base cost 10)...");
    console.log(bestiary.buy_beast('knight_mount'));
    console.log(`Coins remaining: ${bestiary.coins}`);
    console.log("-".repeat(20));

    // --- SCENARIO 3: HARD DIFFICULTY ---
    console.log("\n--- Scenario: Hard Difficulty ---");
    modes_manager.set_difficulty('hard');
    console.log(`Difficulty changed to: ${modes_manager.difficulty}`);
    ai_brain.player_moves = []; // Reset moves
    bestiary.coins = 20; // Reset coins

    // Demonstrate AI twist (more sensitive)
    console.log("\nSimulating player dodging (more sensitive)...");
    ai_brain.learn_move('attack');
    ai_brain.learn_move('attack');
    ai_brain.learn_move('attack');
    ai_brain.learn_move('dodge');
    console.log("AI response (1 dodge in last 4):", ai_brain.throw_twist());

    // Demonstrate beast cost (more expensive)
    console.log("\nAttempting to buy a knight_mount (base cost 10)...");
    console.log(bestiary.buy_beast('knight_mount'));
    console.log(`Coins remaining: ${bestiary.coins}`);
}

run_game_scenario();
