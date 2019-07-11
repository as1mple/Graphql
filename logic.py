import asyncio

from aiohttp import ClientSession

import json

from setting import save_data


async def http_request(session: ClientSession, json_data,
                       ) -> dict:
    url = "https://www.homeaway.com/serp/g"

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    hhh = {'User-Agent': ua}
    async with session.post(url, headers=hhh, json=json_data) as response:
        resp_data = await response.read()
        print(resp_data)
        resp_json = json.loads(resp_data)
        return resp_json


async def build_post_json(listing_id):
    """Json"""
    return {
        "operationName": "imagesForListing",
        "variables": {
            "listingId": listing_id,
        },
        "query": '''query imagesForListing($listingId: String!) {   listing(listingId: $listingId){
    address{
      country
      city
    }
    ownersListingProfile{
      aboutYou
      whyHere
      storyPhoto
      yearPurchased
      uniqueBenefits
    }
   contact{
    name
    languagesSpoken
    ownerProfilePhoto
    memberSince
    redirectUrl
    hasPhoneNumber
    phones{
      phoneNumber
    }

    }
  }
}'''
    }


async def run(ID):
    tasks = []
    async with ClientSession() as session:
        for tmp in ID:
            task = asyncio.ensure_future(head(tmp, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses


async def head(id: str, session: ClientSession) -> None:
    js = await build_post_json(id)
    tmp = await http_request(session, js)
    print(tmp)
    save_data(tmp)
