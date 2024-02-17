// default package
// Generated 26 nov 2023 19:40:10 by Hibernate Tools 5.2.13.Final
package enginerinversed.entities;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 * Message generated by hbm2java
 */
@Entity
@Table(name = "Message", catalog = "kurigram")
public class Message implements java.io.Serializable {

	private int id;
	private Conversation conversation;
	private User userByIduser;
	private User userBySenderIduser;
	private Date createdAt;
	private String text;
	private Set<Conversation> conversations = new HashSet<Conversation>(0);

	public Message() {
	}

	public Message(int id, User userBySenderIduser) {
		this.id = id;
		this.userBySenderIduser = userBySenderIduser;
	}

	public Message(int id, Conversation conversation, User userByIduser, User userBySenderIduser, Date createdAt,
			String text, Set<Conversation> conversations) {
		this.id = id;
		this.conversation = conversation;
		this.userByIduser = userByIduser;
		this.userBySenderIduser = userBySenderIduser;
		this.createdAt = createdAt;
		this.text = text;
		this.conversations = conversations;
	}

	@Id

	@Column(name = "id", unique = true, nullable = false)
	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "conversation_id")
	public Conversation getConversation() {
		return this.conversation;
	}

	public void setConversation(Conversation conversation) {
		this.conversation = conversation;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "iduser")
	public User getUserByIduser() {
		return this.userByIduser;
	}

	public void setUserByIduser(User userByIduser) {
		this.userByIduser = userByIduser;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "sender_iduser", nullable = false)
	public User getUserBySenderIduser() {
		return this.userBySenderIduser;
	}

	public void setUserBySenderIduser(User userBySenderIduser) {
		this.userBySenderIduser = userBySenderIduser;
	}

	@Temporal(TemporalType.TIMESTAMP)
	@Column(name = "created_at", length = 19)
	public Date getCreatedAt() {
		return this.createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	@Column(name = "text")
	public String getText() {
		return this.text;
	}

	public void setText(String text) {
		this.text = text;
	}

	@OneToMany(fetch = FetchType.LAZY, mappedBy = "message")
	public Set<Conversation> getConversations() {
		return this.conversations;
	}

	public void setConversations(Set<Conversation> conversations) {
		this.conversations = conversations;
	}

}
