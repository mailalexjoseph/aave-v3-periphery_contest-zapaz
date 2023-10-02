/////////////////////////////////////////////////////////////////////////////////
// Ensure claimAllRewards is same as two getUserRewards , with ONE asset TWO rewards
// but timeout...
/////////////////////////////////////////////////////////////////////////////////
rule rewardsTwoClaimAllRewardsAsExpected(env e, address[] assets, address user, address to) {
    require rewardsTwoAssetsOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards@withrevert(e, assets, to);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimAllRewardsToSelf is same as two getUserRewards , with ONE asset TWO rewards
// but timeout...
/////////////////////////////////////////////////////////////////////////////////
rule rewardsTwoClaimAllRewardsToSelfAsExpected(env e, address[] assets, address user) {
    require rewardsTwoAssetsOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf@withrevert(e, assets);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}
/////////////////////////////////////////////////////////////////////////////////
// Ensure claimAllRewardsOnBehalf is same as two getUserRewards , with ONE asset TWO rewards
// but timeout...
/////////////////////////////////////////////////////////////////////////////////
rule rewardsTwoClaimAllRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to) {
    require rewardsTwoAssetsOne(assets[0], Reward, RewardB);
    require e.msg.sender == getClaimer(user);

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf@withrevert(e, assets, user, to);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}
