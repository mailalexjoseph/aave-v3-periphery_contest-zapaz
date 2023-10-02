/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewardsToSelf equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsToSelfAsExpected(env e, address[] assets, address user, uint256 amount) {
    require rewardsOneAssetsOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, user);

    mathint amount_ = claimRewardsToSelf(e, assets, amount, Reward);

    mathint balance_ = Reward.balanceOf(e, user);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewardsOnBehalf equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    mathint amount_ = claimRewardsOnBehalf(e, assets, amount, user, to, Reward);

    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewards equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    mathint amount_ = claimRewards(e, assets, amount, to, Reward);

    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewardsOnBehalf equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, assets, user, to);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewards equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetsOne(assets[0], Reward);

    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, assets, to);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewardsToSelf equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsToSelfAsExpected(env e, address[] assets, address user) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, user);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, assets);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, user);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure getAllUserRewards is equal to getUserRewards for ONE asset ONE reward
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimUserRewards(env e, address[] assets, address user){
    // require rewardsOneAssetsOne(assets[0], reward);
    require assets.length == 1;
    require getAvailableRewardsCount(assets[0]) == 1;

    address[] rewardsList = getRewardsList();
    require rewardsList.length == 1;
    require rewardsList[0] == Reward;

    address[] rewardsByAsset = getRewardsByAsset(assets[0]);
    require rewardsByAsset.length == 1;
    require rewardsByAsset[0] == Reward;

    mathint _claimable = getUserRewards(e, assets, user, Reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);
    mathint claimable_ = amounts[0];

    assert claimable_ == _claimable;
}


/////////////////////////////////////////////////////////////////////////////////
// OK       37s https://prover.certora.com/output/56914/652340fee7a044599f5a3054ed89c63f/?anonymousKey=a0ab8951ce65871dcacfbef280f8394f474cc88b
// OK       38s https://prover.certora.com/output/56914/c2f7d6ae9909452e9738178687522cb9/?anonymousKey=350747cd8766872f955a640fe434fcf7e35c1522
// TIMOUT  739s https://prover.certora.com/output/56914/93073387cc7b4c4699650b24d70e1b46/?anonymousKey=f3ed401d017db4fdf66c3226a85d33c256128d1f
// TIMOUT  679s https://prover.certora.com/output/56914/0e4aeb9356f94352bb1575418f42cad5/?anonymousKey=1e6aaf9497bf4a2770ddda8e2c219c42bfcb7cf9
/////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////
// Ensure claiming twice (in same block) cannot increase amount claimed
// - sum of two claims is less than expected claim
// - if first amount more than claimable, first claim gets all rewards, second claim zero
// - if first amount less than claimable, first claim gets exactly amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimTwice(env e, address[] assets, address user, address to, uint256 amount1, uint256 amount2) {
    require assets.length == 1;
    require assets[0] == AToken;

    address[] rewardsByAsset = getRewardsByAsset(assets[0]);

    require rewardsByAsset[0] == Reward;
    require rewardsByAsset.length == 1;

    mathint amount = amount1;
    mathint claimable = getUserRewards(e, assets, user, Reward);
    mathint claimedFirst = claimRewardsOnBehalf(e, assets, amount1, user, to, Reward);
    mathint claimedSecond = claimRewardsOnBehalf(e, assets, amount2, user, to, Reward);

    assert ( claimedFirst + claimedSecond ) <= claimable;
    assert ( amount >= claimable ) => ( claimedFirst == claimable ) && ( claimedSecond == 0 );
    assert ( amount <= claimable ) => ( claimedFirst == amount );
}
