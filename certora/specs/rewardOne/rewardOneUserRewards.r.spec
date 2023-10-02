/////////////////////////////////////////////////////////////////////////////////
// Ensure user rewards stricly equals reward in rewards calculation function
//  for one AToken and one Reward
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneUserRewards(env e, address[] assets, address user) {
    require rewardsOneAssetsOne(AToken, Reward);
    require assets[0] == AToken;
    require assets.length == 1;

    assert getUserRewards(e, assets, user, Reward) == userRewardsCalculate(e, user, Reward);
}




