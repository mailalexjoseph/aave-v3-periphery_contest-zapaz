/////////////////////////////////////////////////////////////////////////////////
// Ensure you can configure ONE asset and ONE reward
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneConfigureAsset(env e, calldataarg args) {
    address[] _assets = getAssetsList();

    require EMISSION_MANAGER() == currentContract;   // must be emission manager to call external function harnessed
    require getLastUpdateTimestamp(AToken,Reward) == 0;
    require getAvailableRewardsCount(AToken) == 0;
    require getAssetDecimals(AToken) == 0;
    require AToken.decimals(e) > 0;
    require _assets.length == 0;
    require isRewardEnabled(Reward) == false;

    configureAsset(e, AToken, Reward, TransferStrategy);

    address[] assets_ = getAssetsList();
    address asset_     = assets_[0];
    address[] rewards_ = getRewardsByAsset(asset_);
    address reward_    = rewards_[0];

    assert getTransferStrategy(Reward) == TransferStrategy;
    assert getRewardOracle(Reward) == rewardOracle();
    assert assets_.length == 1;
    assert rewards_.length == 1;
    assert asset_ == AToken;
    assert reward_ == Reward;
    assert getAvailableRewardsCount(AToken) == 1;
    assert getAssetDecimals(AToken) == AToken.decimals(e);
    assert isRewardEnabled(Reward) == true;
}
