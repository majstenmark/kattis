
    vi dp(n+1);
    rep(i,1,n+1){
        ll aMax = stAmax.query(comp[b[i-1]],2*n);
        ll bMax = stBmax.query(0,comp[b[i-1]]);
        /*rep(j,0,i-1){
            if(a[j]>b[i-1])
                aMax = max(aMax, dp[j]-pref[j]);
            else
                bMax = max(bMax, dp[j]-pref[j]+a[j]);
        }*/
        dp[i] = max(aMax+pref[i-1]+b[i-1], bMax+pref[i-1]);

        stAmax.update(comp[a[i-1]],max(dp[i-1]-pref[i-1],stAmax.query(comp[a[i-1]],comp[a[i-1]]+1)));
        stBmax.update(comp[a[i-1]],max(dp[i-1]-pref[i-1]+a[i-1],stBmax.query(comp[a[i-1]],comp[a[i-1]]+1)));
    }