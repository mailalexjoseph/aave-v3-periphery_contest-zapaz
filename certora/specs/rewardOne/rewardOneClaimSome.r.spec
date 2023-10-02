/////////////////////////////////////////////////////////////////////////////////
// Ensure you can get rewards when all requirements are met
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimSome(env e, address[] assets, address user, address reward) {
    require assets[0] == AToken;
    require assets.length == 1;

    mathint currentTimestamp = e.block.timestamp;
    mathint totalSupply = AToken.totalSupply(e);
    mathint balance = AToken.balanceOf(e, user);
    mathint userIndex = getUserAssetIndex(user, AToken, reward);
    mathint assetIndex;
    mathint emissionPerSecond;
    mathint lastUpdateTimestamp;
    mathint distributionEnd;
    assetIndex, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, AToken, reward);

    require balance > 0;
    require totalSupply >= balance;
    require assetIndex >= userIndex;
    require currentTimestamp < distributionEnd;
    require emissionPerSecond * (e.block.timestamp - lastUpdateTimestamp) > totalSupply;

    assert getUserRewards(e, assets, user, reward) > 0;
}
