/////////////////////////////////////////////////////////////////////////////////
// Ensure claim on 2 assets via claimRewardsToSelf is sum of two claims
/////////////////////////////////////////////////////////////////////////////////
rule assetsTwoClaimRewards(env e) {
    address[] assets = getAssetsList();
    require assets.length == 2;
    require assets[0] != assets[1];
    // require getTransferStrategy(Reward) != to;

    address[] assets1 = [assets[0]];
    address[] assets2 = [assets[1]];
    uint256 claimable = getUserRewards(e, assets, e.msg.sender, Reward);

    mathint amount  = claimRewardsToSelf(e, assets, claimable, Reward);
    mathint amount1  = claimRewardsToSelf(e, assets1, claimable, Reward);
    mathint amount2  = claimRewardsToSelf(e, assets2, claimable, Reward);

    assert amount == amount1 + amount2;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claim on 2 assets via claimAllRewardsToSelf is sum of two claims
/////////////////////////////////////////////////////////////////////////////////
rule assetsTwoClaimAllRewards(env e) {
    address[] assets;
    require assets.length == 2;
    require assets[0] != assets[1];

    address[] assets1 = [assets[0]];
    address[] assets2 = [assets[1]];

    address[] rewards = getRewardsList();
    require rewards.length == 1;

    address[] rewards0; uint256[] amounts0;
    rewards0, amounts0 = claimAllRewardsToSelf(e, assets);
    mathint amount = amounts0[0];

    address[] rewards1; uint256[] amounts1;
    rewards1, amounts1 = claimAllRewardsToSelf(e, assets1);
    mathint amount1 = amounts1[0];

    address[] rewards2; uint256[] amounts2;
    rewards2, amounts2 = claimAllRewardsToSelf(e, assets2);
    mathint amount2 = amounts2[0];

    assert amount == amount1 + amount2;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure accrued on 2 assets via getUserAccruedRewards is sum of two claims
/////////////////////////////////////////////////////////////////////////////////
rule assetsTwoGetUserAccruedRewards(address user) {
    address[] assets = getAssetsList();
    require assets.length == 2;
    require assets[0] != assets[1];

    mathint amount = getUserAccruedRewards(user, Reward);
    mathint amount1 = getUserAccruedReward(0, user, Reward);
    mathint amount2 = getUserAccruedReward(1, user, Reward);

    assert amount == amount1 + amount2;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimable on 2 assets via getAllUserRewards is sum of two claimables
/////////////////////////////////////////////////////////////////////////////////
rule assetsTwoGetAllUserRewards(env e, address user) {
    address[] assets = getAssetsList();
    require assets.length == 2;
    require assets[0] != assets[1];

    address[] assets1 = [assets[0]];
    address[] assets2 = [assets[1]];

    address[] rewards0; uint256[] amounts0;
    rewards0, amounts0 = getAllUserRewards(e, assets, user);
    mathint amount = amounts0[0];

    address[] rewards1; uint256[] amounts1;
    rewards1, amounts1 = getAllUserRewards(e, assets1, user);
    mathint amount1 = amounts1[0];

    address[] rewards2; uint256[] amounts2;
    rewards2, amounts2 = getAllUserRewards(e, assets2, user);
    mathint amount2 = amounts2[0];

    assert amount == amount1 + amount2;
}
