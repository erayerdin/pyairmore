# Messaging Service

`MessagingService` helps you send and manage messages.

To create `MessagingService`, simply do:

    from pyairmore.services.messaging import MessagingService
    service = MessagingService(session)

## Fetching Latest Messages

`fetch_message_history` method will return a `list` of `Message` objects.
To fetch latest messages, see below:

    messages = service.fetch_message_history()
    messages  # a list of Message objects
    messages[0].content  # "Lorem ipsum dolor sit amet..."

A `Message` object holds the properties below:

| Name | Type | Default | Description |
|------|------|---------|-------------|
| id       | str               | None                 | Defined by Airmore server. |
| name     | str               | None                 | How it is seen in your contacts or message header. |
| phone    | str               | None                 | If the message has a header, `phone` will hold the header. |
| datetime | datetime.datetime | None                 |   |
| content  | str               | None                 |   |
| type     | MessageType       | MessageType.RECEIVED |   |
| was_read | bool              | True                 |   |
| count    | int               | 1                    |   |

 > #### Tip
 > `MessageType` is an `Enum`, under `pyairmore.services.messaging` module.
 > It defines if the message was received or sent, so it has two values:
 > either `RECEIVED` or `SENT`.

 > #### Further Tip
 > You can also compare `Message` objects if they are `equal`, `older` or
 > `newer` via comparison operators.

## Fetching A Particular Chat

You can also fetch a particular chat that a `Message` is in. You can do this
via `fetch_chat_history`. This method's signature is a bit different than
`fetch_message_history`.

 > #### Signature: `MessagingService::fetch_chat_history`
 > | Name | Type | Default | Description |
 > |------|------|---------|-------------|
 > | message_or_id | `Message` or `str` | -  |   |
 > | start         | int                | 0  | Where fetching will start from. |
 > | limit         | int                | 10 | Where fetching will end. |

You have to either pass a `Message` object or a `str` defining the ID of
message.

`start` with default value `0` will fetch from the latest message in the
chat history. If it was `1`, the latest message would be excluded.

`limit` defines how many messages to fetch in total.

 > #### Tip
 > If it exceeds the total messages in a chat history, then whole history
 > will be fetched.

 > #### Note
 > `fetch_chat_history` and `fetch_message_history` will return a `list` of
 > `Message` objects in a historically descending order.
 >
 > Also, whatever `Message` object or `id` you provide to
 > `fetch_chat_history`, you will always receive the *whole* chat history.
 > `start` parameter will make the difference about where the history starts.

For example, let's get the `Message` object to a variable in the example
above:

    message = messages[0]
    
Now we might pass it to `fetch_chat_history`:

    chat = service.fetch_chat_history(message)
    chat  # a list of Message objects again
    len(chat)  # 10
    chat[0] == message  # True, assuming `message` is the latest message

## Sending Message

`send_message` method will send a message to a phone number you provide.

 > #### Signature: `MessagingService::send_message`
 > | Name | Type | Default | Description |
 > |------|------|---------|-------------|
 > | contact_or_phone | str | -  | `contact` will be provided in a future release. |
 > | content          | str | -  |   |

To send a message:

    service.send_message("123456", "foo bar baz")

This method will raise `MessageRequestGSMError` if sending fails and will
always return `None`.
