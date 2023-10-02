/////////////////////////////////////////////////////////////////////////////////
// Reward calculation function for ONE reward and ONE asset (AToken)
/////////////////////////////////////////////////////////////////////////////////
function userRewardsCalculate(env e, address user, address reward) returns uint256 {
    uint256 totalSupply = AToken.scaledTotalSupply(e);
    uint8 decimals = getAssetDecimals(AToken);
    uint256 assetUnit = require_uint256(10^decimals);

    uint256 __assetIndex; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    __assetIndex, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, AToken, reward);

    uint256 _assetIndex; uint256 _assetIndexOld;
    _assetIndexOld, _assetIndex = getAssetIndex(e, AToken, reward);
    assert _assetIndexOld == __assetIndex;

    uint104 assetIndex = require_uint104(_assetIndex);
    uint88 emissionPerSecond = require_uint88(_emissionPerSecond);
    uint32 lastUpdateTimestamp = require_uint32(_lastUpdateTimestamp);
    uint32 distributionEnd = require_uint32(_distributionEnd);

    uint32 currentTimestamp = require_uint32(e.block.timestamp);
    uint128 userAccrued = require_uint128(getUserAccruedRewards(user, reward));
    uint104 userIndex = require_uint104(getUserAssetIndex(user, AToken, reward));
    uint256 userBalance = AToken.balanceOf(e, user);

    require userBalance > 0;
    require totalSupply > userBalance;
    require currentTimestamp < distributionEnd;
    require currentTimestamp > lastUpdateTimestamp;

    uint256 claimable = userRewardCalculate(e, currentTimestamp, lastUpdateTimestamp, emissionPerSecond,
                              assetIndex, userIndex, userAccrued, userBalance , totalSupply, assetUnit);

    return claimable;
}

