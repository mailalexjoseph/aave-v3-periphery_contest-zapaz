/////////////////////////////////////////////////////////////////////////////////
// lastUpdateTimestamp should always be before current timestamp
/////////////////////////////////////////////////////////////////////////////////
invariant timestamp(env e, address asset, address reward)
    getLastUpdateTimestamp(asset, reward) <= e.block.timestamp
    { preserved with (env ep) { require  ep.block.timestamp == e.block.timestamp; } }

/////////////////////////////////////////////////////////////////////////////////
// reward should be enabled if and only if in rewards list
/////////////////////////////////////////////////////////////////////////////////
invariant rewardEnabled(address reward)
    isRewardEnabled(reward) <=> inArray(getRewardsList(), reward);

/////////////////////////////////////////////////////////////////////////////////
// asset rewards count should be less than overall rewards list length
// didn't succeed to make forall quantifier working...
/////////////////////////////////////////////////////////////////////////////////
// invariant rewardsLength(address asset)
//     getRewardsByAssetLength(asset) <= getRewardsListLength()
//     filtered { f -> !f.isView && !harnessFunction(f) }
//     { preserved {
//         require (forall address reward . isRewardEnabled(reward) <=> inArray( getRewardsList(), reward) );
//     } }
